for file in ./debug/pred*
do
	python evaluate_squad.py --prediction_file "$file" --dataset_file "hotpot/hp_dev.squad" >> results.out
done
