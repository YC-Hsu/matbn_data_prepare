#!/bin/bash

. ./cmd.sh
. ./path.sh

if [ $# != 3 ]; then
   echo "Usage: $0 [options] <lang-dir> <lm-file> <lm-dir>";
   echo "e.g.: $0 data/lang local/normal/lm/srilm.o3g.kn data/lang_test"
   echo "options: "
   echo "				"
   exit 1;
fi

lang_dir=$1
lm_file=$2
lm_dir=$3

# Be careful: this time we dispense with the grep -v '<s> <s>' so this might
# not work for LMs generated from all toolkits.
  arpa2fst --natural-base=false $lm_file | fstprint | \
    utils/eps2disambig.pl | utils/s2eps.pl | fstcompile --isymbols=$lang_dir/words.txt \
      --osymbols=$lang_dir/words.txt  --keep_isymbols=false --keep_osymbols=false | \
     fstrmepsilon > $lang_dir/G.fst || exit 1;
  fstisstochastic $lang_dir/G.fst
  
  utils/validate_lang.pl $lang_dir

rm -r $lm_dir
cp -r $lang_dir $lm_dir

# grep -v '<s> <s>' etc. is only for future-proofing this script.  Our
# LM doesn't have these "invalid combinations".  These can cause 
# determinization failures of CLG [ends up being epsilon cycles].
# Note: remove_oovs.pl takes a list of words in the LM that aren't in
# our word list.  Since our LM doesn't have any, we just give it
# /dev/null [we leave it in the script to show how you'd do it].
cat $lm_file | \
   grep -v '<s> <s>' | \
   grep -v '</s> <s>' | \
   grep -v '</s> </s>' | \
   arpa2fst --natural-base=false - | fstprint | \
   utils/remove_oovs.pl /dev/null | \
   utils/eps2disambig.pl | utils/s2eps.pl | fstcompile --isymbols=$lm_dir/words.txt \
     --osymbols=$lm_dir/words.txt  --keep_isymbols=false --keep_osymbols=false | \
    fstrmepsilon > $lm_dir/G.fst
  fstisstochastic $lm_dir/G.fst
echo  "Checking how stochastic G is (the first of these numbers should be small):"
fstisstochastic $lm_dir/G.fst 

## Check lexicon.
## just have a look and make sure it seems sane.
echo "First few lines of lexicon FST:"
fstprint   --isymbols=$lang_dir/phones.txt --osymbols=$lang_dir/words.txt $lang_dir/L.fst  | head
exit 0;
