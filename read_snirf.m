function read_snirf( filenm )

if ~exist( 'filenm' )
    [filenm,pathnm] = uigetfile( '*.snirf', 'Choose NIRS files to convert to SNIRF', 'MultiSelect', 'on' );
    if ~iscell(filenm)
        if filenm==0
            return
        end
    end
end

if ~iscell(filenm)
    if ~exist(filenm,'file')
        disp( sprintf(' %s does not exist as a file.',filenm) );
        return
    end
end



nFiles = 1;
if iscell(filenm)
    nFiles = length(filenm);
end

for iFile = 1:nFiles
    % Load file
    if ~iscell(filenm)
        d=h5read(filenm,'/data/d')
        t=h5read(filenm,'/data/t')
        ml=h5read(filenm,'/data/ml')

        SD.lambda=h5read(filenm,'/SD/Lambda')
        SD.SrcPos=h5read(filenm,'/SD/SrcPos')
        SD.DetPos=h5read(filenm,'/SD/DetPos')
        
        stimnames=h5read(filenm,'/stim/ConditionName')
        stimdata=h5read(filenm,'/stim/Data')
        
        attr=h5info(filenm);
        attrlist=attr.Attributes
        numattr=length(attr.Attributes)
        for theattr = 1:numattr
            mytuple=[attrlist(theattr).Name, attrlist(theattr).Value]
        end

    else
        d=h5read(filenm{iFile},'/data/d')
        t=h5read(filenm{iFile},'/data/t')
        ml=h5read(filenm{iFile},'/data/ml')
    end
end
    
