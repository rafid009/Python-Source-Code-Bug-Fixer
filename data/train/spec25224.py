import numpy as np 

def function(x):

	j3 = 8
	f0 = 9
	paths = []
	try:
		if j3 <= 4:
			j3 = j3/5
			x = x*0
			f0 = 0*4
			paths.append(1)
		else:
			x = f0-x
			f0 = 5+3
			paths.append(2)
		if f0 > 2:
			f0 = 5-f0
			f0 = f0-0
			paths.append(3)
		else:
			f0 = 8*f0
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))