import numpy as np 

def function(x):

	d6 = x
	l7 = 5
	paths = []
	try:
		if l7 > 1:
			d6 = d6+x
			paths.append(1)
		else:
			l7 = l7+9
			x = x+3
			paths.append(2)
		if d6 <= 8:
			x = x-2
			l7 = l7-3
			d6 = d6-7
			paths.append(3)
		else:
			d6 = x+d6
			d6 = 9-d6
			l7 = x+1
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		l7 = d6**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))