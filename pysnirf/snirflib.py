#!/opt/local/bin/python
#
#       $Author: frederic $
#       $Date: 2013/08/30 18:39:43 $
#       $Id: snirflib.py,v 1.3 2013/08/30 18:39:43 frederic Exp $
#
from __future__ import print_function

import h5py as h5py
import numpy as np
import string
    
ml_dtype = np.dtype ( [ ('SourceIndex', np.uint32),
                           ('DetectorIndex', np.uint32),
                           ('WavelengthIndex', np.uint32),
                           ('DataType', np.uint32),
                           ('DataTypeIndex', np.uint32) ] )
#                           ('SourcePower', np.float64),
#                           ('DetectorGain', np.float64) ] )

pos_dtype = np.dtype ( [ ( 'x', np.float64),
                            ( 'y', np.float64),
                            ( 'z', np.float64) ] )

stim_data_dtype = np.dtype ( [('start', np.float64),
                ('duration', np.float64),
                ('value', np.float64) ] )

#namestring_dtype = h5py.special_dtype(vlen=str)
namestring_dtype = np.dtype ( [ ( 'Name', 'U64') ] )

def padstring(num):
    return (str(num).zfill(5))

def make_ml_array(nchans):
    return np.zeros((nchans,), dtype=ml_dtype)

def make_stim_arrays(numconditions):
    the_stimname = np.zeros((1,), dtype=namestring_dtype)
    the_stimdata = np.zeros((numconditions,), dtype=stim_data_dtype)
    return(the_stimname,the_stimdata)

def make_aux_arrays(ntimepoints):
    the_aux_tvec = np.zeros((ntimepoints,), dtype=np.float64)
    the_aux_dvec = np.zeros((ntimepoints,), dtype=np.float64)
    the_auxname = np.zeros((1,), dtype=namestring_dtype)
    return(the_aux_tvec,the_aux_dvec,the_auxname)

def make_data_arrays(ntimepoints):
    the_data_tvec = np.zeros((ntimepoints,),dtype=np.float64)
    the_data_dvec = np.zeros((ntimepoints,),dtype=np.float64)
    the_ml = np.zeros((1,), dtype=ml_dtype)
    return(the_data_tvec,the_data_dvec,the_ml)

def make_SD_arrays(numlambdas,numlambdaex,numsrc,numdet):
    the_SD_lambdas = np.zeros((numlambdas,),dtype=np.float64)
    the_SD_lambdaex = np.zeros((numlambdaex,),dtype=np.float64)
    the_SD_srcpos = np.zeros((numsrc,),dtype=pos_dtype)
    the_SD_detpos = np.zeros((numdet,),dtype=pos_dtype)
    the_SD_srclabels = np.zeros((numsrc,),dtype='a64')
    the_SD_detlabels = np.zeros((numdet,),dtype='a64')
    return(the_SD_lambdas,the_SD_lambdaex,the_SD_srcpos,the_SD_detpos,the_SD_srclabels,the_SD_detlabels)

def readgroup(fileptr,basename):
    # read back and construct the data struct
    thevals=[]
    idx=0
    done=False
    while(not done):
        recname=basename+padstring(idx)
        try:
            thevals.append(fileptr[recname])
        except KeyError:
            done=True
        else:
            idx=idx+1
    return thevals

def read_snirf(name):
    thehdf = h5py.File(name,'r')

    Compliant=True
    fileversion = thehdf.attrs['format_version']
    if (fileversion != 1.0):
        print("incorrect file version number")
        Compliant=False

    # read back and construct the data struct
    thedata=readgroup(thehdf,'/data/')
    nelements=len(thedata)
    # check to see if there is at least one dataset
    if(nelements>0):
        print(nelements, " data elements detected")
    else:
        Compliant=False
        print("FILE INVALID - required structure missing: data")
    # check to see that each dataset has all required fields
    for thedataset in thedata:
        thedataattrs=thedataset.attrs.items()
        for item in ['SourceIndex','DetectorIndex','WavelengthIndex','DataType','DataTypeIndex']:
            testval = thedataset.attrs.get(item)
            if (testval==''):
                print("MEASUREMENT INVALID - required datasete attribute missing: ",item)
                Compliant=False

    # read back and construct the SD struct
    try:
        theSD=thehdf['/SD']
    except KeyError:
        theSD=[]
        print("FILE INVALID - required structure missing: SD")
        Compliant=False

    # read back and construct the data struct
    thestims=readgroup(thehdf,'/stim/')
    nelements=len(thestims)
    if(nelements>0):
        print(nelements, " stim elements detected")
    else:
        Compliant=False
        print("FILE INVALID - required structure missing: stim")

    # read back the aux
    theauxs=readgroup(thehdf,'/aux/')
    nelements=len(theauxs)
    if(nelements>0):
        print(nelements, " optional aux elements detected")

    # read the file attributes
    theattrs=thehdf.attrs.items()
    print(theattrs)

    metagroup=thehdf['/metadata/']
    themetaattrs=metagroup.attrs.items()
    testval = metagroup.attrs.get('SpatialUnit')
    if (testval==''):
        print("FILE INVALID - required tag missing: SpatialUnit")
        Compliant=False

    testval = metagroup.attrs.get('MeasurementDate')
    if (testval==''):
        print("FILE INVALID - required tag missing: MeasurementData")
        Compliant=False

    testval = metagroup.attrs.get('MeasurementTime')
    if (testval==''):
        print("FILE INVALID - required tag missing: MeasurementTime")
        Compliant=False

    testval = metagroup.attrs.get('SubjectID')
    if (testval==''):
        print("FILE INVALID - required tag missing: SubjectID")
        Compliant=False

    return Compliant,thedata,theSD,thestims,theattrs,themetaattrs,theauxs

def write_snirf(name,thisdata,thisSD,thisstim,metadict,theaux=[], debug=False):

    # open up a file for writing
    thehdf = h5py.File(name,'w')

    # add in the mandatory attributes
    thehdf.attrs['format_version']=1.0

    # add in the optional metadata attributes
    metadatagroup=thehdf.create_group('metadata')
    for metaitems in metadict:
        metadatagroup.attrs[metaitems]=metadict[metaitems]

    # add the structures to the data group
    datagroup=thehdf.create_group('data')
    for i in range(0,len(thisdata)):
        if debug:
            print('creating group', padstring(i))
        dataidx=datagroup.create_group(padstring(i))
        dataidx['d']=thisdata[i]['d']
        dataidx['t']=thisdata[i]['t']
        dataidx.attrs['SourceIndex']=thisdata[i]['ml']['SourceIndex']
        dataidx.attrs['DetectorIndex']=thisdata[i]['ml']['DetectorIndex']
        dataidx.attrs['WavelengthIndex']=thisdata[i]['ml']['WavelengthIndex']
        dataidx.attrs['DataType']=thisdata[i]['ml']['DataType']
        dataidx.attrs['DataTypeIndex']=thisdata[i]['ml']['DataTypeIndex']
        try:
            dataidx.attrs['SourcePower']=thisdata[i]['ml']['SourcePower']
        except ValueError:
            pass
        try:
            dataidx.attrs['DetectorGain']=thisdata[i]['ml']['DetectorGain']
        except ValueError:
            pass

    # add the structures to the stim group
    stimgroup=thehdf.create_group('stim')
    for i in range(0,len(thisstim)):
        stimidx=stimgroup.create_group(padstring(i))
        stimidx['Name']=np.copy(thisstim[i]['Name'])
        stimidx['Data']=thisstim[i]['Data']

    # write out the SD
    SDgroup=thehdf.create_group('SD')
    SDgroup['Lambda']=thisSD['Lambda']
    SDgroup['LambdaExcitation']=thisSD['LambdaExcitation']
    SDgroup['SrcPos']=thisSD['SrcPos']
    SDgroup['DetPos']=thisSD['DetPos']
    SDgroup['SrcLabels']=thisSD['SrcLabels']
    SDgroup['DetLabels']=thisSD['DetLabels']

    # write out the aux
    if (theaux != []):
        auxgroup=thehdf.create_group('aux')
        for i in range(0,len(theaux)):
            auxidx=auxgroup.create_group(padstring(i))
            auxidx['d']=theaux[i]['d']
            auxidx['t']=theaux[i]['t']
            auxidx['Name']=theaux[i]['Name']

    # clean up
    thehdf.close()
    
def print_SD(theSD):
    print('Lambdas:')
    numlambda=len(theSD['Lambda'])
    for i in range(0,numlambda):
        print(theSD['Lambda'][i])
    print('LambdaExcitation:')
    numlambdaex=len(theSD['LambdaExcitation'])
    for i in range(0,numlambdaex):
        print(theSD['LambdaExcitation'][i])
    print('SrcPos:')
    numsrc=len(theSD['SrcPos'])
    for i in range(0,numsrc):
        print(theSD['SrcLabels'][i],theSD['SrcPos'][i])
    print('DetPos:')
    numdet=len(theSD['DetPos'])
    for i in range(0,numdet):
        print(theSD['DetLabels'][i],theSD['DetPos'][i])
    print

def print_stim(thestims):
    print(thestims['Name'].value)
    for i in range(0,len(thestims['Data']['start'])):
        print(thestims['Data']['start'][i],thestims['Data']['duration'][i],thestims['Data']['value'][i])
    print

def print_aux(thereadaux):
    print(thereadaux['Name'].value)
    print(thereadaux['t'][:])
    print(thereadaux['d'][:])
    print

def print_ml(theml):
    print('SourceIndex:',theml['SourceIndex'])
    print('DetectorIndex:', theml['DetectorIndex'])
    print('WavelengthIndex:', theml['WavelengthIndex'])
    print('DataType:', theml['DataType'])
    print('DataTypeIndex:', theml['DataTypeIndex'])
    #print('SourcePower:', theml['SourcePower'])
    #print('DetectorGain:', theml['DetectorGain'])

def print_measurement(thereaddata):
    #print_ml(thereaddata['ml'])
    print(thereaddata['t'][:])
    print(thereaddata['d'][:])
    theattrs=thereaddata.attrs.items()
    for item in ['SourceIndex','DetectorIndex','WavelengthIndex','DataType','DataTypeIndex']:
        testval = thereaddata.attrs.get(item)
        if (testval==''):
            print("MEASUREMENT INVALID - required attribute missing: ",item)
        else:
            print(item,': ',testval)
    for item in ['SourcePower','DetectorGain']:
        testval = thereaddata.attrs.get(item)
        if (testval!=''):
            print(item,': ',testval)
    print
