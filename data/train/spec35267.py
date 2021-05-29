import numpy as np 

def function(x):

	f4 = x
	v4 = x
	x = x
	paths = []
	try:
		if x < 8:
			x = x*0
			paths.append(1)
		else:
			v4 = 2+v4
			f4 = 1*3
			x = 5/2
			paths.append(2)
		if f4 <= 8:
			x = v4*x
			paths.append(3)
		else:
			f4 = x/x
			f4 = v4/f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		v4 = f4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))