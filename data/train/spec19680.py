import numpy as np 

def function(x):

	p6 = x
	j2 = 4
	paths = []
	try:
		if j2 <= 6:
			x = x+j2
			j2 = p6*j2
			paths.append(1)
		else:
			x = x+1
			p6 = j2-j2
			paths.append(2)
		if j2 >= 3:
			p6 = 3/p6
			x = 5-4
			p6 = p6-p6
			paths.append(3)
		else:
			p6 = 9/2
			x = x-7
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		p6 = j2**0.5
		return p6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))