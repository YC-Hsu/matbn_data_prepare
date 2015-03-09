words=data/lang/words.txt

if [ $# != 2 ]; then
   echo "Usage: $0 [options] <data-dir> <lang-dir>";
   echo "e.g.: $0 data_tone/lang data_tone/lang_test"
   echo "options: "
   echo "		"
   exit 1;
fi

data_dir=$1
lang_dir=$2
words=$data_dir/words.txt

mkdir -p $data_dir
rm -rf $lang_dir
cp -r $data_dir $lang_dir

echo "prepare $data_dir/G.fst ..."
echo "creating $data_dir/G.txt ..."
python local/py_code/CreateFile_G.txt_tone.py $data_dir
echo "creating file $data_dir/G.fst ..."
fstcompile --isymbols=$words --osymbols=$words --keep_isymbols=false \
			--keep_osymbols=false $data_dir/G.txt > $data_dir/G.fst
echo "delete file $data_dir/G.txt ..."
rm -rf $data_dir/G.txt

echo "prepare $lang_dir/G.fst ..."
echo "creating $lang_dir/G.txt ..."
python local/py_code/CreateFile_G.txt_tone.py $lang_dir
echo "creating file $lang_dir/G.fst ..."
fstcompile --isymbols=$words --osymbols=$words --keep_isymbols=false \
			--keep_osymbols=false $lang_dir/G.txt > $lang_dir/G.fst
echo "delete file $lang_dir/G.txt ..."
rm -rf $lang_dir/G.txt

