import numpy as np 

def function(x):

	n7 = x
	l3 = x
	paths = []
	try:
		if n7 > 0:
			x = n7*0
			x = x+4
			l3 = l3-2
			paths.append(1)
		else:
			x = n7/n7
			paths.append(2)
		if l3 <= 4:
			n7 = n7-3
			x = x*l3
			paths.append(3)
		else:
			n7 = n7-7
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		l3 = n7**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))