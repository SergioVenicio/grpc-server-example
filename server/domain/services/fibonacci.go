package services

import (
	"github.com/sergiovenicio/grpc-server-example/domain/entities"
	"github.com/sergiovenicio/grpc-server-example/domain/repositories"
)

var cache = make(map[int64]int64)

func fib(number int64) int64 {
	cached, exists := cache[number]
	if exists {
		return cached
	}
	if number <= 1 {
		return number
	}
	result := fib(number-1) + fib(number-2)
	cache[number] = result
	return result
}

type FibonacciService struct {
	repository *repositories.FibonacciRepository
}

func (s *FibonacciService) Register(request *entities.CalcRequest) {
	s.repository.Add(request)
}

func (s *FibonacciService) Find(id string) (*entities.CalcRequest, error) {
	request, err := s.repository.Get(id)
	if err != nil {
		return nil, err
	}

	return request, nil
}

func (s *FibonacciService) Calc(request *entities.CalcRequest) {
	dbRequest, err := s.repository.Get(request.Id)
	if err != nil {
		return
	}
	if dbRequest.Status == "COMPLETED" || dbRequest.Status == "FAILED" {
		return
	}
	dbRequest.Status = "STARTED"
	s.repository.Add(dbRequest)
	dbRequest.Result = fib(dbRequest.Number)
	dbRequest.Status = "COMPLETED"
	s.repository.Add(dbRequest)
}

func NewFibonacciService(fibonacciRepo *repositories.FibonacciRepository) *FibonacciService {
	return &FibonacciService{
		repository: fibonacciRepo,
	}
}
