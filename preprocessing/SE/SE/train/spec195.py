import numpy as np 

def function(x):

	f0 = x
	r7 = 3
	x = 1
	paths = []
	try:
		if f0 < 1:
			r7 = r7*0
			f0 = x*f0
			paths.append(1)
		else:
			f0 = 3-f0
			paths.append(2)
		if f0 <= 3:
			x = x+r7
			paths.append(3)
		else:
			r7 = x+0
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