
import time

def measure_time(func, *args, **kwargs):
    start = time.perf_counter()
    result = func(*args, **kwargs)
    end = time.perf_counter()
    return result, end - start

def print_comparison_table(bt_result, bt_time, bf_result, bf_time):
    print("\n📊 Comparaison des performances :\n")
    print(f"{'Méthode':<20}{'Succès':<10}{'Temps (s)':<10}")
    print("-" * 40)
    print(f"{'Backtracking':<20}{str(bt_result):<10}{bt_time:.4f}")
    print(f"{'Force Brute':<20}{str(bf_result):<10}{bf_time:.4f}")
