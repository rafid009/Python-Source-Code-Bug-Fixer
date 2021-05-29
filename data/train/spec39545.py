import numpy as np 

def function(x):

	f5 = x
	v2 = 7
	paths = []
	try:
		if x < 4:
			f5 = 0/5
			f5 = v2-8
			paths.append(1)
		else:
			x = x+f5
			paths.append(2)
		if f5 >= 9:
			v2 = 0-v2
			f5 = f5*7
			f5 = f5+v2
			paths.append(3)
		else:
			v2 = v2-5
			x = x+5
			f5 = v2/f5
			paths.append(4)
		paths.append(5)
		assert f5 >= 0
		x = f5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))