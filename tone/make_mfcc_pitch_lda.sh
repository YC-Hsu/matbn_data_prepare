
if [ $# != 4 ]; then
   echo "Usage: $0 [options] <keyword> <read-dir> <write-dir> <ark-dir>";
   echo "e.g.: $0 train data/train data_tone/train mfcc_pitch_lda"
   echo "options: "
   echo "				"
   exit 1;
fi

keyword=$1
read_dir=$2
write_dir=$3
ark_dir=$4

mkdir -p $ark_dir

splice-feats --left-context=4 --right-context=4 \
	scp:$read_dir/feats.scp \
	ark,scp:$ark_dir/$keyword.ark,$write_dir/feats_lda.scp

