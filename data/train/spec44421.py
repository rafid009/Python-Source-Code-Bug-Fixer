import numpy as np 

def function(x):

	v3 = x
	l5 = x
	paths = []
	try:
		if l5 > 2:
			x = x-1
			paths.append(1)
		else:
			l5 = x*0
			paths.append(2)
		if x < 9:
			v3 = 3/v3
			x = x*0
			x = 7*v3
			paths.append(3)
		else:
			l5 = l5/l5
			v3 = x/7
			paths.append(4)
		paths.append(5)
		assert v3 >= 0
		l5 = v3**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))