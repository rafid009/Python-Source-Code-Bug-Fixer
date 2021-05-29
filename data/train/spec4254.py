import numpy as np 

def function(x):

	f9 = x
	d5 = x
	paths = []
	try:
		if f9 >= 3:
			f9 = d5*f9
			f9 = f9*5
			f9 = f9+f9
			paths.append(1)
		else:
			f9 = f9-6
			paths.append(2)
		if f9 > 1:
			d5 = 2/d5
			d5 = d5*1
			x = 9/d5
			paths.append(3)
		else:
			d5 = d5-5
			f9 = x*f9
			d5 = d5/9
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))