import numpy as np 

def function(x):

	f7 = 1
	t6 = 2
	paths = []
	try:
		if x < 9:
			f7 = 3-6
			t6 = t6*t6
			paths.append(1)
		else:
			x = x-0
			x = 1+f7
			paths.append(2)
		if x > 1:
			f7 = 6-f7
			t6 = t6+5
			paths.append(3)
		else:
			t6 = t6*f7
			f7 = 2+t6
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		f7 = t6**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))