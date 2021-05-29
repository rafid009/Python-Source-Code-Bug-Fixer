import numpy as np 

def function(x):

	r0 = 7
	i3 = x
	x = 7
	paths = []
	try:
		if i3 >= 4:
			r0 = 7/r0
			i3 = i3+8
			paths.append(1)
		else:
			x = 4-x
			r0 = i3+2
			paths.append(2)
		if i3 > 1:
			r0 = 6*r0
			x = 2+1
			paths.append(3)
		else:
			r0 = r0+i3
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		i3 = i3**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))