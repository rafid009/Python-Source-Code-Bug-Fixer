import numpy as np 

def function(x):

	m1 = 0
	t7 = x
	paths = []
	try:
		if m1 <= 8:
			m1 = 5/4
			x = t7*3
			x = x/6
			paths.append(1)
		else:
			x = 0-m1
			paths.append(2)
		if m1 <= 3:
			x = x*0
			x = x*1
			m1 = m1-0
			paths.append(3)
		else:
			m1 = m1+5
			x = t7*x
			paths.append(4)
		paths.append(5)
		assert t7 >= 0
		t7 = t7**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))