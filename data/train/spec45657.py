import numpy as np 

def function(x):

	n1 = x
	i3 = x
	paths = []
	try:
		if i3 > 4:
			n1 = n1+5
			paths.append(1)
		else:
			x = x+i3
			n1 = n1+5
			paths.append(2)
		if n1 <= 6:
			x = x/9
			x = i3-x
			paths.append(3)
		else:
			n1 = n1+x
			n1 = 9+i3
			n1 = n1-9
			paths.append(4)
		paths.append(5)
		assert i3 >= 0
		n1 = i3**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))