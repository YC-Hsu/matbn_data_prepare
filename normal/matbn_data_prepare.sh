


if [ $# != 4 ]; then
   echo "Usage: $0 [options] <train-dir> <dev-dir> <test-dir> <corpus-dir>";
   echo "e.g.: $0 data/train data/dev data/test /mnt/corpus/MATBN"
   echo "options: "
   echo "				"
   exit 1;
fi

train_dir=$1
dev_dir=$2
test_dir=$3
corpus_dir=$4

mkdir -p $train_dir $dev_dir $test_dir

echo "prepare matbn $train_dir ..."
echo "prepare file $train_dir/text ..."
cp $corpus_dir/LABEL/label_tr.ark $train_dir/text
echo "prepare file $train_dir/wav.scp ..."
python local/py_code/CreateFile_wav.scp_.py $corpus_dir/MATBN_TRAIN $train_dir/wav.scp
echo "prepare file utt2spk ..."
python local/py_code/CreateFile_utt2spk_.py $train_dir
echo "prepare file spk2utt ..."
utils/utt2spk_to_spk2utt.pl $train_dir/utt2spk > $train_dir/spk2utt
utils/fix_data_dir.sh $train_dir

echo "prepare matbn $dev_dir ..."
echo "prepare file $dev_dir/text ..."
cp $corpus_dir/LABEL/label_dev.ark $dev_dir/text
echo "prepare file $dev_dir/wav.scp ..."
python local/py_code/CreateFile_wav.scp_.py $corpus_dir/MATBN_DEV_292 $dev_dir/wav.scp
echo "prepare file utt2spk ..."
python local/py_code/CreateFile_utt2spk_.py $dev_dir
echo "prepare file spk2utt ..."
utils/utt2spk_to_spk2utt.pl $dev_dir/utt2spk > $dev_dir/spk2utt
utils/fix_data_dir.sh $dev_dir

echo "prepare matbn $test_dir ..."
echo "prepare file $test_dir/text ..."
cp $corpus_dir/LABEL/label_ev.ark $test_dir/text
echo "prepare file $test_dir/wav.scp ..."
python local/py_code/CreateFile_wav.scp_.py $corpus_dir/MATBN_EVAL_307 $test_dir/wav.scp
echo "prepare file utt2spk ..."
python local/py_code/CreateFile_utt2spk_.py $test_dir
echo "prepare file spk2utt ..."
utils/utt2spk_to_spk2utt.pl $test_dir/utt2spk > $test_dir/spk2utt
utils/fix_data_dir.sh $test_dir
