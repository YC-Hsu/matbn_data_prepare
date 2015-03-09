
if [ $# != 5 ]; then
   echo "Usage: $0 [options] <keyword> <read-dir> <segments-file> <write-dir> <ark-dir>";
   echo "e.g.: $0 train data_tone/train data_tone/train/segments data_tone/train mfcc_pitch_segments"
   echo "options: "
   echo "				"
   exit 1;
fi

keyword=$1
read_dir=$2
segments_file=$3
write_dir=$4
ark_dir=$5

mkdir -p $ark_dir

extract-feature-segments --min-segment-length=0.002 \
	scp:$read_dir/feats_lda.scp \
	$segments_file \
	ark,scp:$ark_dir/$keyword.ark,$write_dir/feats.scp


