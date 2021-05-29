import numpy as np 

def function(x):

	a2 = x
	i3 = 7
	paths = []
	try:
		if a2 > 7:
			i3 = i3+6
			i3 = a2*8
			paths.append(1)
		else:
			x = 5/7
			i3 = 1+i3
			paths.append(2)
		if i3 >= 1:
			a2 = a2*x
			i3 = 3-i3
			i3 = x+2
			paths.append(3)
		else:
			a2 = 1*a2
			x = x+3
			i3 = i3*8
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		i3 = a2**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))