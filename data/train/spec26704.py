import numpy as np 

def function(x):

	t2 = x
	f6 = 4
	paths = []
	try:
		if t2 > 5:
			f6 = f6+2
			x = 2*x
			x = x-f6
			paths.append(1)
		else:
			t2 = t2+3
			t2 = t2+7
			f6 = x*t2
			paths.append(2)
		if f6 > 6:
			x = t2+8
			paths.append(3)
		else:
			f6 = 5-8
			t2 = t2-7
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		x = f6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))