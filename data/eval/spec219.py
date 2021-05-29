import numpy as np 

def function(x):

	l3 = 8
	m5 = x
	paths = []
	try:
		if m5 <= 0:
			l3 = l3-m5
			l3 = l3*x
			m5 = m5*8
			paths.append(1)
		else:
			l3 = l3*0
			m5 = m5+7
			paths.append(2)
		if x < 8:
			m5 = 8-8
			m5 = m5+x
			paths.append(3)
		else:
			l3 = m5-l3
			l3 = x-1
			paths.append(4)
		paths.append(5)
		assert m5 >= 0
		x = m5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))