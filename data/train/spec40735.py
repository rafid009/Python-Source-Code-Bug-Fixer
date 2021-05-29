import numpy as np 

def function(x):

	j1 = 1
	p4 = 4
	paths = []
	try:
		if x > 3:
			x = x/5
			paths.append(1)
		else:
			p4 = j1*p4
			x = x*1
			j1 = 6-j1
			paths.append(2)
		if j1 >= 8:
			p4 = x+p4
			p4 = 2+1
			p4 = 1*2
			paths.append(3)
		else:
			j1 = x/4
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		j1 = j1**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))