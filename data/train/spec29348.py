import numpy as np 

def function(x):

	l5 = 4
	j2 = x
	paths = []
	try:
		if j2 >= 8:
			j2 = j2-0
			j2 = 4/j2
			paths.append(1)
		else:
			j2 = 4/9
			paths.append(2)
		if l5 > 2:
			j2 = j2-1
			x = l5+j2
			l5 = l5*1
			paths.append(3)
		else:
			l5 = 3/l5
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		j2 = j2**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))