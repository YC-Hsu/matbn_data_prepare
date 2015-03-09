if [ $# != 8 ]; then
   echo "Usage: $0 [options] <phone-file> <train-dir> <train-ali> <dev-dir> <dev-ali> <test-dir> <test-ali> <corpus-dir>";
   echo "e.g.: $0 data/lang/phones.txt data_tone/train exp/mono0a_train_ali data_tone/dev exp/mono0a_dev_ali data_tone/test exp/mono0a_test_ali /mnt/corpus/MATBN"
   echo "options: "
   echo "				"
   exit 1;
fi

phone_file=$1
train_dir=$2
train_ali=$3
dev_dir=$4
dev_ali=$5
test_dir=$6
test_ali=$7
corpus_dir=$8

mkdir -p $train_dir $dev_dir $test_dir
mkdir -p $train_ali/tmp $dev_ali/tmp $test_ali/tmp

echo "prepare matbn $train_dir ..."
echo "prepare file $train_dir/text ..."
gunzip -c $train_ali/ali.*.gz > $train_ali/tmp/ali.txt
show-transitions $phone_file $train_ali/final.mdl > $train_ali/tmp/state_and_phone.txt
python local/py_code/CreateFile_text_tone.py $train_ali/tmp/state_and_phone.txt $train_ali/tmp/ali.txt $train_dir/text
echo "prepare file $train_dir/wav.scp ..."
python local/py_code/CreateFile_wav.scp_.py $corpus_dir/MATBN_TRAIN $train_dir/wav.scp
echo "prepare file $train_dir/segments ..."
python local/py_code/CreateFile_segments_tone.py $train_dir
echo "prepare file utt2spk ..."
python local/py_code/CreateFile_utt2spk_tone.py $train_dir
echo "prepare file spk2utt ..."
utils/utt2spk_to_spk2utt.pl $train_dir/utt2spk > $train_dir/spk2utt
utils/fix_data_dir.sh $train_dir

echo "prepare matbn $dev_dir ..."
echo "prepare file $dev_dir/text ..."
gunzip -c $dev_ali/ali.*.gz > $dev_ali/tmp/ali.txt
show-transitions $phone_file $dev_ali/final.mdl > $dev_ali/tmp/state_and_phone.txt
python local/py_code/CreateFile_text_tone.py $dev_ali/tmp/state_and_phone.txt $dev_ali/tmp/ali.txt $dev_dir/text
echo "prepare file $dev_dir/wav.scp ..."
python local/py_code/CreateFile_wav.scp_.py $corpus_dir/MATBN_DEV_292 $dev_dir/wav.scp
echo "prepare file $dev_dir/segments ..."
python local/py_code/CreateFile_segments_tone.py $dev_dir
echo "prepare file utt2spk ..."
python local/py_code/CreateFile_utt2spk_tone.py $dev_dir
echo "prepare file spk2utt ..."
utils/utt2spk_to_spk2utt.pl $dev_dir/utt2spk > $dev_dir/spk2utt
utils/fix_data_dir.sh $dev_dir

echo "prepare matbn $test_dir ..."
echo "prepare file $test_dir/text ..."
gunzip -c $test_ali/ali.*.gz > $test_ali/tmp/ali.txt
show-transitions $phone_file $test_ali/final.mdl > $test_ali/tmp/state_and_phone.txt
python local/py_code/CreateFile_text_tone.py $test_ali/tmp/state_and_phone.txt $test_ali/tmp/ali.txt $test_dir/text
echo "prepare file $test_dir/wav.scp ..."
python local/py_code/CreateFile_wav.scp_.py $corpus_dir/MATBN_EVAL_307 $test_dir/wav.scp
echo "prepare file $test_dir/segments ..."
python local/py_code/CreateFile_segments_tone.py $test_dir
echo "prepare file utt2spk ..."
python local/py_code/CreateFile_utt2spk_tone.py $test_dir
echo "prepare file spk2utt ..."
utils/utt2spk_to_spk2utt.pl $test_dir/utt2spk > $test_dir/spk2utt
utils/fix_data_dir.sh $test_dir

echo "delete $train_ali/tmp $dev_ali/tmp $test_ali/tmp ..."
rm -rf $train_ali/tmp $dev_ali/tmp $test_ali/tmp
