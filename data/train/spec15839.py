import numpy as np 

def function(x):

	i5 = 0
	l3 = x
	paths = []
	try:
		if x >= 3:
			l3 = 2-l3
			i5 = x+2
			i5 = i5*l3
			paths.append(1)
		else:
			l3 = l3/5
			l3 = l3*0
			i5 = i5*l3
			paths.append(2)
		if i5 < 8:
			l3 = x*l3
			l3 = l3/2
			paths.append(3)
		else:
			i5 = i5-9
			paths.append(4)
		paths.append(5)
		assert l3 >= 0
		i5 = l3**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))