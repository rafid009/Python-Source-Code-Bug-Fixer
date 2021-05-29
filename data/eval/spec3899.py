import numpy as np 

def function(x):

	f9 = x
	j8 = x
	paths = []
	try:
		if f9 <= 5:
			j8 = j8+5
			x = x-5
			f9 = f9/6
			paths.append(1)
		else:
			f9 = f9-8
			paths.append(2)
		if x >= 0:
			j8 = 1-0
			j8 = 7-j8
			paths.append(3)
		else:
			x = x*6
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