import numpy as np 

def function(x):

	i3 = 3
	b2 = 0
	paths = []
	try:
		if b2 >= 1:
			i3 = i3*7
			b2 = x*4
			paths.append(1)
		else:
			i3 = b2*0
			x = x+x
			paths.append(2)
		if b2 > 6:
			b2 = b2*x
			i3 = i3/i3
			i3 = x/5
			paths.append(3)
		else:
			i3 = 8-2
			x = x/1
			x = i3-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i3 = x**0.5
		return i3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))