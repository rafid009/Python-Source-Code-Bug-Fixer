import numpy as np 

def function(x):

	f3 = 5
	v0 = x
	paths = []
	try:
		if f3 <= 8:
			f3 = f3-f3
			paths.append(1)
		else:
			f3 = f3+0
			f3 = 5+v0
			paths.append(2)
		if v0 <= 3:
			f3 = 8-x
			x = 3/2
			paths.append(3)
		else:
			v0 = v0/4
			v0 = 2-v0
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		f3 = v0**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))