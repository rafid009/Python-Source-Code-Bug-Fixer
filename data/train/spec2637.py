import numpy as np 

def function(x):

	p9 = 7
	j2 = 3
	paths = []
	try:
		if j2 > 6:
			p9 = x*p9
			j2 = j2-8
			paths.append(1)
		else:
			x = x+x
			x = x-0
			j2 = 1-j2
			paths.append(2)
		if j2 <= 5:
			j2 = 8-x
			paths.append(3)
		else:
			j2 = 8/5
			paths.append(4)
		paths.append(5)
		assert j2 >= 0
		p9 = j2**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))