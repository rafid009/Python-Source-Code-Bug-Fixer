import numpy as np 

def function(x):

	r8 = x
	v6 = 4
	paths = []
	try:
		if x >= 8:
			r8 = r8-8
			v6 = r8/v6
			x = 8/5
			paths.append(1)
		else:
			v6 = v6+v6
			paths.append(2)
		if x < 7:
			x = x+6
			r8 = r8+5
			paths.append(3)
		else:
			x = r8+9
			x = 5/r8
			v6 = 6+x
			paths.append(4)
		paths.append(5)
		assert r8 >= 0
		v6 = r8**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))