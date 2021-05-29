import numpy as np 

def function(x):

	k2 = x
	t6 = 4
	paths = []
	try:
		if k2 <= 2:
			t6 = 8-9
			t6 = x+k2
			k2 = k2+7
			paths.append(1)
		else:
			x = 2-7
			t6 = t6/7
			x = x*x
			paths.append(2)
		if t6 > 2:
			t6 = t6+k2
			paths.append(3)
		else:
			t6 = t6-7
			t6 = 7/t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		t6 = t6**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))