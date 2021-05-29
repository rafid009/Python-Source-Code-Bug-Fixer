import numpy as np 

def function(x):

	i0 = x
	a4 = 8
	paths = []
	try:
		if i0 > 2:
			i0 = x+4
			a4 = 5*a4
			x = x*4
			paths.append(1)
		else:
			a4 = x/a4
			i0 = a4*2
			i0 = 4+i0
			paths.append(2)
		if a4 > 4:
			i0 = i0-7
			x = 0+x
			a4 = a4-4
			paths.append(3)
		else:
			i0 = 3+i0
			i0 = 8+a4
			i0 = i0*0
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		i0 = a4**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))