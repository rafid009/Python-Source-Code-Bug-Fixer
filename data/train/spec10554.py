import numpy as np 

def function(x):

	n1 = x
	j2 = 7
	paths = []
	try:
		if j2 < 1:
			j2 = j2/2
			paths.append(1)
		else:
			x = x*1
			n1 = n1*2
			paths.append(2)
		if j2 > 7:
			n1 = n1+5
			j2 = j2-3
			j2 = j2-x
			paths.append(3)
		else:
			j2 = j2-8
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		j2 = n1**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))