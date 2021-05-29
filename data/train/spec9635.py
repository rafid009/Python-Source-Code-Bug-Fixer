import numpy as np 

def function(x):

	v1 = x
	r0 = x
	paths = []
	try:
		if v1 < 5:
			r0 = r0*6
			r0 = 2*v1
			paths.append(1)
		else:
			r0 = 0/r0
			paths.append(2)
		if v1 >= 4:
			x = x+1
			r0 = r0+r0
			v1 = v1-8
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		v1 = v1**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))