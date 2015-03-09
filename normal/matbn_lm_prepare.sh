


if [ $# != 2 ]; then
   echo "Usage: $0 [options] <data-dir> <lang-dir>";
   echo "e.g.: $0 data/lang data/lang_test"
   echo "options: "
   echo "		"
   exit 1;
fi

data_dir=$1
lang_dir=$2

target_dir=/home/deer/kaldi-trunk/egs/matbn/s1/data

rm -rf $data_dir $lang_dir

cp -r $target_dir/lang $data_dir
cp -r $target_dir/lang_test $lang_dir


echo "Succeeded preparing grammar for MATBN."

