def sum_string(string):
    list_chars = [zerone for zerone in string if zerone in ["0", "1"]]
    return list_chars


def check_triads(trio, final_str):
    list_occur_zero = [i for i in range(len(final_str)) if final_str.startswith(trio + '0', i)]
    list_occur_one = [i for i in range(len(final_str)) if final_str.startswith(trio + '1', i)]

    return [len(list_occur_zero), len(list_occur_one)]


number_str = ""
list_str = []
list_triads = ['000', '001', '010', '011', '100', '101', '110', '111']

while len(list_str) < 100:
    print('Print a random string containing 0 or 1:')
    number_str = input()
    list_str.extend(sum_string(number_str))

    if len(list_str) < 100:
        print(f'Current data length is {len(list_str)}, {(100 - len(list_str))} symbols left')

print("\nFinal data string:")
final_st = ''.join(list_str)
print(f"{final_st}\n")

for tri in list_triads:
    values = check_triads(tri, final_st)
    print(f"{tri}: {values[0]},{values[1]}")


