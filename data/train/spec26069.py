import numpy as np 

def function(x):

	f2 = 6
	t3 = x
	paths = []
	try:
		if f2 < 2:
			t3 = t3*4
			paths.append(1)
		else:
			f2 = f2/7
			t3 = t3+3
			paths.append(2)
		if x <= 1:
			x = x*4
			t3 = 7/4
			x = t3+x
			paths.append(3)
		else:
			f2 = 7*t3
			f2 = f2*9
			t3 = 8+t3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))