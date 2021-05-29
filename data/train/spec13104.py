import numpy as np 

def function(x):

	t1 = 9
	k9 = x
	paths = []
	try:
		if t1 > 3:
			t1 = t1/k9
			paths.append(1)
		else:
			k9 = k9*2
			paths.append(2)
		if t1 < 2:
			t1 = 4-x
			k9 = k9-8
			x = x+5
			paths.append(3)
		else:
			k9 = k9*1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		k9 = t1**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))