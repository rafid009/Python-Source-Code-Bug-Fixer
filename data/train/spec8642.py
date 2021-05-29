import numpy as np 

def function(x):

	t7 = 0
	k6 = x
	paths = []
	try:
		if t7 >= 9:
			k6 = 8+k6
			t7 = k6+x
			x = x-5
			paths.append(1)
		else:
			x = x*3
			t7 = 8/9
			t7 = k6+0
			paths.append(2)
		if k6 <= 8:
			k6 = 0/k6
			paths.append(3)
		else:
			t7 = 8-4
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		x = t7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))