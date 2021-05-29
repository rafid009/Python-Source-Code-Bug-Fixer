import numpy as np 

def function(x):

	i8 = 1
	f0 = 9
	paths = []
	try:
		if f0 > 2:
			x = x/8
			paths.append(1)
		else:
			x = 4-8
			paths.append(2)
		if x < 2:
			f0 = 1-f0
			paths.append(3)
		else:
			x = 4/2
			x = 6+4
			x = i8*0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		f0 = f0**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))