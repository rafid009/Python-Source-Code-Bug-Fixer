import numpy as np 

def function(x):

	f4 = x
	v1 = x
	paths = []
	try:
		if x < 9:
			v1 = v1-4
			v1 = x+v1
			paths.append(1)
		else:
			f4 = f4*v1
			v1 = x*v1
			v1 = v1+x
			paths.append(2)
		if f4 <= 4:
			v1 = v1*7
			v1 = v1/4
			x = 5+x
			paths.append(3)
		else:
			f4 = f4*v1
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		x = v1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))