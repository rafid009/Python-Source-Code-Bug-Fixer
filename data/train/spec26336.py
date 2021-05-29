import numpy as np 

def function(x):

	l9 = x
	j2 = 7
	paths = []
	try:
		if l9 > 9:
			j2 = j2*l9
			l9 = l9-l9
			j2 = j2-1
			paths.append(1)
		else:
			j2 = 4*5
			paths.append(2)
		if j2 < 1:
			x = j2-x
			l9 = 9/3
			j2 = j2/9
			paths.append(3)
		else:
			l9 = x-3
			j2 = j2-j2
			j2 = j2*j2
			paths.append(4)
		paths.append(5)
		assert l9 >= 0
		x = l9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))