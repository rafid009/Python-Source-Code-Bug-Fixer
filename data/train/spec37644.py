import numpy as np 

def function(x):

	r6 = 7
	i3 = x
	x = 2
	paths = []
	try:
		if r6 >= 1:
			x = 7+3
			i3 = 8+i3
			paths.append(1)
		else:
			r6 = 6*r6
			x = x/9
			x = 9*i3
			paths.append(2)
		if i3 <= 2:
			x = i3/3
			i3 = 6-9
			paths.append(3)
		else:
			x = 0*1
			x = x*6
			r6 = r6/7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))