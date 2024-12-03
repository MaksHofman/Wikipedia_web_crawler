package main

import (
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

// A set to keep track of visited URLs
var visited = make(map[string]bool)

func crawl(wikipediaURL string, depth int) {
	if depth <= 0 {
		return
	}

	// Check if the URL has already been visited
	if visited[wikipediaURL] {
		return
	}
	visited[wikipediaURL] = true

	fmt.Printf("Crawling: %s\n", wikipediaURL)

	// Fetch the webpage
	resp, err := http.Get(wikipediaURL)
	if err != nil {
		log.Printf("Failed to fetch URL %s: %v\n", wikipediaURL, err)
		return
	}
	defer resp.Body.Close()

	// Check HTTP status
	if resp.StatusCode != 200 {
		log.Printf("Non-200 HTTP status for %s: %d\n", wikipediaURL, resp.StatusCode)
		return
	}

	// Parse the HTML using goquery
	doc, err := goquery.NewDocumentFromReader(resp.Body)
	if err != nil {
		log.Printf("Failed to parse HTML for %s: %v\n", wikipediaURL, err)
		return
	}

	// Extract and print the title of the current page
	title := doc.Find("h1#firstHeading").Text()
	fmt.Printf("Title: %s\n", title)

	// Find all links to other Wikipedia articles
	doc.Find("a").Each(func(i int, s *goquery.Selection) {
		link, exists := s.Attr("href")
		if !exists {
			return
		}

		// Ensure the link is a valid Wikipedia article URL
		if strings.HasPrefix(link, "/wiki/") && !strings.Contains(link, ":") {
			absoluteURL := "https://en.wikipedia.org" + link
			crawl(absoluteURL, depth-1) // Recursively crawl the linked page
		}
	})
}

func main() {
	// Seed URL (starting point)
	seedURL := "https://en.wikipedia.org/wiki/Web_scraping"

	// Set the crawl depth
	maxDepth := 2

	// Start crawling
	crawl(seedURL, maxDepth)
}
