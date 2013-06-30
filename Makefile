all: test_hh_perf_low test_hh_perf_med test_hh_perf_hgh actual_answer
actual_answer:
	time cat ./stats/test/heavy_hitters.log | sort | uniq -c | sort -n | awk '{print $$2, $$1}' | tail -1
test_hh_perf_low:
	time ./bin/heavy -n 100 ./stats/test/heavy_hitters.log | tail -1
test_hh_perf_med:
	time ./bin/heavy -n 1000 ./stats/test/heavy_hitters.log | tail -1 
test_hh_perf_hgh:
	time ./bin/heavy -n 64000 ./stats/test/heavy_hitters.log | tail -1 
