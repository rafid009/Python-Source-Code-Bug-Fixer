import numpy as np 

def function(x):

	j2 = 5
	p7 = 8
	x = x
	paths = []
	try:
		if p7 > 8:
			p7 = p7+j2
			x = x*1
			x = x/5
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if p7 < 1:
			x = x+3
			p7 = p7+j2
			paths.append(3)
		else:
			j2 = j2/p7
			p7 = p7+2
			p7 = x-p7
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		j2 = p7**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))