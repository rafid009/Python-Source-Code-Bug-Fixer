import numpy as np 

def function(x):

	m1 = 3
	h1 = x
	paths = []
	try:
		if m1 <= 3:
			x = 6/x
			h1 = 2/h1
			x = h1/m1
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x <= 9:
			h1 = 4/h1
			m1 = m1*2
			h1 = h1+x
			paths.append(3)
		else:
			x = x*0
			m1 = m1*2
			paths.append(4)
		paths.append(5)
		assert h1 >= 0
		m1 = h1**0.5
		return m1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))