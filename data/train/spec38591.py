import numpy as np 

def function(x):

	v3 = x
	r3 = x
	x = x
	paths = []
	try:
		if x < 9:
			v3 = 3*v3
			r3 = r3+4
			paths.append(1)
		else:
			v3 = v3-2
			v3 = 9*3
			paths.append(2)
		if x <= 5:
			r3 = 2-0
			paths.append(3)
		else:
			r3 = x*r3
			r3 = r3-7
			x = x+1
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		r3 = v3**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))