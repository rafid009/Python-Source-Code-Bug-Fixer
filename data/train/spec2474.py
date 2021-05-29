import numpy as np 

def function(x):

	f6 = 8
	h9 = x
	x = x
	paths = []
	try:
		if f6 >= 1:
			x = 6*x
			f6 = 2+f6
			x = f6/x
			paths.append(1)
		else:
			f6 = 1+f6
			x = x-f6
			paths.append(2)
		if h9 > 1:
			h9 = f6*h9
			f6 = x/f6
			f6 = x-4
			paths.append(3)
		else:
			f6 = 6+1
			f6 = 4/h9
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert f6 >= 0
		f6 = f6**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))